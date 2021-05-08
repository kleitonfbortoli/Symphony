import React from 'react'

import {ErrorMessage, Formik, Form, Field} from 'formik'
import * as yup from 'yup'

import { System } from '../../system/system'
import { Message } from '../../system/message'
import { POST_CADASTRO_TIPO_NOTA } from '../../system/constants'

import '../../styles/scss/pages/basic/forms.scss'

const CadastroTipoNota = () => {
    const handleSubmit = (values => {
        System.post(POST_CADASTRO_TIPO_NOTA, values, (data) => {
            Message.showMessage("Tipo de nota salvo com sucesso");
        });
    });
    
    const validations = yup.object().shape({
        descricao: yup.string().required()
    })

    return (
        <>
            <div className="form">
                <h1 className="form-title">Cadastro Tipo de nota</h1>
                <p className="form-subtitle">Preencha os campos para continuar</p>
                <Formik initialValues={{}} onSubmit={handleSubmit} validationSchema={validations}>
                    <Form className="form-body">
                        <div className="field-group">
                            <Field name="descricao" className="field" placeholder="Descricao"/>
                            <ErrorMessage component="span" name="descricao" className="field-error"/>
                        </div>
                        <button className="submit-button" type="submit">Salvar</button>
                    </Form>
                </Formik>
            </div>
        </>
    )
}

export default CadastroTipoNota