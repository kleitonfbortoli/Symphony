import React from 'react'

import {ErrorMessage, Formik, Form, Field} from 'formik'
import * as yup from 'yup'
import axios from 'axios'

import '../../styles/scss/pages/basic/forms.scss'

const CadastroTipoNota = () => {
    const handleSubmit = values => (
        axios.post('http://localhost:8000/cadastro-tipo-nota', values)
            .then(resp => {
                console.log(resp)
            })
            .catch(error => {
                console.log('Erro')
                console.log(error)
            })
    )
    
    const validations = yup.object().shape({
        descricao: yup.string().required(),
        campo: yup.number().required()
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
                        <div className="field-group">
                            <Field name="campo" className="field" placeholder="Campo"/>
                            <ErrorMessage component="span" name="campo" className="field-error"/>
                        </div>
                        <button className="submit-button" type="submit">Salvar</button>
                    </Form>
                </Formik>
            </div>
        </>
    )
}

export default CadastroTipoNota