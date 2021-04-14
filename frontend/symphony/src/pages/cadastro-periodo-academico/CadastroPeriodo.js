import React from 'react'

import {ErrorMessage, Formik, Form, Field} from 'formik'
import * as yup from 'yup'

import { System } from '../../system/system'
import { Message } from '../../system/message'
import { POST_CADASTRO_PERIODO_ACADEMICO } from '../../system/constants'

import '../../styles/scss/pages/basic/forms.scss'

const CadastroPeriodo = () => {
    const handleSubmit = (values => {
        System.post(POST_CADASTRO_PERIODO_ACADEMICO, values, (data) => {
            Message.showMessage("Período Acadêmico salvo com sucesso!");
        });
    });
    
    const validations = yup.object().shape({
        descricao: yup.string().required(),
        dt_inicio: yup.date().required(),
        dt_final: yup.date().required()
    })

    return (
        <>
            <div className="form">
                <h1 className="form-title">Cadastro Período</h1>
                <p className="form-subtitle">Preencha os campos para continuar</p>
                <Formik initialValues={{}} onSubmit={handleSubmit} validationSchema={validations}>
                    <Form className="form-body">
                        <div className="field-group">
                            <Field name="descricao" className="field" placeholder="Descrição"/>
                            <ErrorMessage component="span" name="descricao" className="field-error"/>
                        </div>
                        <div className="field-group">
                            <Field name="dt_inicio" className="field" placeholder="Data Inicial"/>
                            <ErrorMessage component="span" name="dt_inicio" className="field-error"/>
                        </div>
                        <div className="field-group">
                            <Field name="dt_final" className="field" placeholder="Data Final"/>
                            <ErrorMessage component="span" name="dt_final" className="field-error"/>
                        </div>
                        <button className="submit-button" type="submit">Enviar</button>
                    </Form>
                </Formik>
            </div>
        </>
    )
}

export default CadastroPeriodo