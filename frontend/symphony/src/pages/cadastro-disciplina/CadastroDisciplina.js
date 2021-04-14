import React from 'react'

import {ErrorMessage, Formik, Form, Field} from 'formik'
import * as yup from 'yup'

import { System } from '../../system/system'
import { Message } from '../../system/message'
import { POST_CADASTRO_DISCIPLINA } from '../../system/constants'

import '../../styles/scss/pages/basic/forms.scss'

const CadastroDisciplina = () => {
    const handleSubmit = (values => {
        System.post(POST_CADASTRO_DISCIPLINA, values, (data) => {
            Message.showMessage("Disicplina salva com sucesso!");
        });
    });
    
    const validations = yup.object().shape({
        nome: yup.string().required(),
        ch: yup.number().required()
    })

    return (
        <>
            <div className="form">
                <h1 className="form-title">Cadastro Disciplina</h1>
                <p className="form-subtitle">Preencha os campos para continuar</p>
                <Formik initialValues={{}} onSubmit={handleSubmit} validationSchema={validations}>
                    <Form className="form-body">
                        <div className="field-group">
                            <Field name="nome" className="field" placeholder="Nome"/>
                            <ErrorMessage component="span" name="nome" className="field-error"/>
                        </div>
                        <div className="field-group">
                            <Field name="ch" className="field" placeholder="Carga Horária"/>
                            <ErrorMessage component="span" name="ch" className="field-error"/>
                        </div>
                        <button className="submit-button" type="submit">Salvar</button>
                    </Form>
                </Formik>
            </div>
        </>
    )
}

export default CadastroDisciplina