import React from 'react'

import {ErrorMessage, Formik, Form, Field} from 'formik'
import * as yup from 'yup'
import axios from 'axios'

import '../../styles/scss/pages/basic/forms.scss'

const CadastroPessoa = () => {
    const handleSubmit = values => (
        axios.post('http://localhost:8000/cadastro-pessoa', values)
            .then(resp => {
                console.log(resp)
            })
            .catch(error => {
                console.log('Erro')
                console.log(error)
            })
    )
    
    const validations = yup.object().shape({
        email: yup.string().email().required(),
        password: yup.string().min(8).required(),
        nome: yup.string().required(),
        dt_nascimento: yup.date().required()
    })

    return (
        <>
            <div className="form">
                <h1 className="form-title">Cadastro Pessoa</h1>
                <p className="form-subtitle">Preencha os campos para continuar</p>
                <Formik initialValues={{}} onSubmit={handleSubmit} validationSchema={validations}>
                    <Form className="form-body">
                        <div className="field-group">
                            <Field name="nome" className="field" placeholder="Nome"/>
                            <ErrorMessage component="span" name="nome" className="field-error"/>
                        </div>
                        <div className="field-group">
                            <Field name="dt_nascimento" className="field" placeholder="Data Nascimentos"/>
                            <ErrorMessage component="span" name="dt_nascimento" className="field-error"/>
                        </div>
                        <div className="field-group">
                            <Field name="email" className="field" placeholder="Email"/>
                            <ErrorMessage component="span" name="email" className="field-error"/>
                        </div>
                        <div className="field-group">
                            <Field name="password" className="field" placeholder="Senha"/>
                            <ErrorMessage component="span" name="password" className="field-error"/>
                        </div>
                        <button className="submit-button" type="submit">Enviar</button>
                    </Form>
                </Formik>
            </div>
        </>
    )
}

export default CadastroPessoa