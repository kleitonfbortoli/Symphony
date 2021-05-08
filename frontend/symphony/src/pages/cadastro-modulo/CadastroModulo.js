import React from 'react'

import {ErrorMessage, Formik, Form, Field} from 'formik'
import * as yup from 'yup'

import { System } from '../../system/system'
import { Message } from '../../system/message'
import { POST_CADASTRO_MODULO } from '../../system/constants'

import '../../styles/scss/pages/basic/forms.scss'

const CadastroModulo = () => {
    const handleSubmit = (values => {
        console.log('s');
        System.post(POST_CADASTRO_MODULO, values, (data) => {
            Message.showMessage("Módulo salvo com sucesso");
        });
    });
    
    const validations = yup.object().shape({
        title: yup.string().required()
    })

    return (
        <>
            <div className="form">
                <h1 className="form-title">Cadastro Módulo</h1>
                <p className="form-subtitle">Preencha os campos para continuar</p>
                <Formik initialValues={{}} onSubmit={handleSubmit} validationSchema={validations}>
                    <Form className="form-body">
                        <div className="field-group">
                            <Field name="title" className="field" placeholder="Título" />
                            <ErrorMessage component="span" name="title" className="field-error" />
                        </div>
                        <button className="submit-button" type="submit">Enviar</button>
                    </Form>
                </Formik>
            </div>
        </>
    )
}

export default CadastroModulo