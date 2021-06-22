import React, { useEffect, useState } from 'react'
import { Message } from '../../system/message'

import { System } from '../../system/system'
import {ErrorMessage, Formik, Form, Field} from 'formik'

import { POST_GET_ALL_PERIODO, POST_GET_ALL_SERIE, POST_CADASTRO_TURMA } from '../../system/constants'

import '../../styles/scss/pages/basic/forms.scss'

const CadastroTurma = () => {
    const handleSubmit = (values => {
        System.post(POST_CADASTRO_TURMA, values, (data) => {
            Message.showMessage("Turma salva com sucesso");
        });
    });

    const [options_periodo, setOptionsPeriodo] = useState([<option></option>])

    function reloadTipoNota() {
        System.post(POST_GET_ALL_PERIODO, {}, (data) => {
            
            const options = [<option></option>];
            
            data.map((obj) => {
                options.push(<option key={obj.key} value={ obj.key}>{obj.label}</option>)
            })

            setOptionsPeriodo(options)
        });
    }

    const [options_serie, setOptionsSerie] = useState([<option></option>])

    function reloadSerie() {
        System.post(POST_GET_ALL_SERIE, {}, (data) => {
            const options = [<option></option>];
            data.map((obj) => {
                options.push(<option key={obj.key} value={ obj.key}>{obj.label}</option>)
            })

            setOptionsSerie(options)
        });
    }

    useEffect(() => {
        reloadTipoNota()
        reloadSerie()
    }, [])

    return (
        <>
            <div className="form">
                <h1 className="form-title">Cadastro Turma</h1>
                <p className="form-subtitle">Preencha os campos para continuar</p>
                <Formik initialValues={{}} onSubmit={handleSubmit}>
                    <Form className="form-body">
                        <div className="field-group">
                            <Field name="descricao" className="field" placeholder="Descrição"/>
                            <ErrorMessage component="span" name="descricao" className="field-error"/>
                        </div>
                        <div className="field-group">
                            <Field name="ref_serie" className="field" placeholder="Série" as="select">
                                { options_serie}
                            </Field>
                            <ErrorMessage component="span" name="serie" className="field-error"/>
                        </div>
                        <div className="field-group">
                            <Field name="ref_periodo" className="field" placeholder="Período" as="select">
                                { options_periodo}
                            </Field>
                            <ErrorMessage component="span" name="tipo" className="field-error"/>
                        </div>
                        <button className="submit-button" type="submit">Salvar</button>
                    </Form>
                </Formik>
            </div>
        </>
    )
}

export default CadastroTurma