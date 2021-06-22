import React, { useEffect, useState } from 'react'

import { System } from '../../system/system'
import {ErrorMessage, Formik, Form, Field} from 'formik'
import * as yup from 'yup'

import { POST_GET_ALL_TIPO_NOTA, POST_GET_ALL_SERIE } from '../../system/constants'

import '../../styles/scss/pages/basic/forms.scss'

const CadastroNota = () => {
    const handleSubmit = (values => {
        // System.post(POST_CADASTRO_NOTA, values, (data) => {
        //     Message.showMessage("Usuário salvo com sucesso");
        // });
    });

    const [options_tipo_nota, setOptionsTipoNota] = useState([<option></option>])

    function reloadTipoNota() {
        System.post(POST_GET_ALL_TIPO_NOTA, {}, (data) => {
            const options = [<option></option>];
            data.map((obj) => {
                options.push(<option key={obj.key} value={ obj.key}>{obj.label}</option>)
            })

            setOptionsTipoNota(options)
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
    
    const validations = yup.object().shape({
        descricao: yup.string().required(),
        ordem: yup.number().required(),
        tipo: yup.number().required(),
        serie: yup.number().required()
    })

    return (
        <>
            <div className="form">
                <h1 className="form-title">Cadastro Nota</h1>
                <p className="form-subtitle">Preencha os campos para continuar</p>
                <Formik initialValues={{}} onSubmit={handleSubmit} validationSchema={validations}>
                    <Form className="form-body">
                        <div className="field-group">
                            <Field name="descricao" className="field" placeholder="Descrição"/>
                            <ErrorMessage component="span" name="descricao" className="field-error"/>
                        </div>
                        <div className="field-group">
                            <Field name="ordem" className="field" placeholder="Ordem"/>
                            <ErrorMessage component="span" name="ordem" className="field-error"/>
                        </div>
                        <div className="field-group">
                            <Field name="tipo" className="field" placeholder="Tipo de nota" as="select">
                                { options_tipo_nota}
                            </Field>
                            <ErrorMessage component="span" name="tipo" className="field-error"/>
                        </div>
                        <div className="field-group">
                            <Field name="serie" className="field" placeholder="Série" as="select">
                                { options_serie}
                            </Field>
                            <ErrorMessage component="span" name="serie" className="field-error"/>
                        </div>
                        <button className="submit-button" type="submit">Salvar</button>
                    </Form>
                </Formik>
            </div>
        </>
    )
}

export default CadastroNota