import React from 'react'

import {ErrorMessage, Formik, Form, Field} from 'formik'
import * as yup from 'yup'
import axios from 'axios'
// import DatePicker from 'react-date-picker'
// import { history } from '../../history'

import './CadastroPessoa.css'

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
        // dt_nascimento: yup.date().min(8).required()
    })

    return (
        <>
            <h1>CadastroPessoa</h1>
            <p>Preencha os campos para continuar</p>
            <Formik initialValues={{}} onSubmit={handleSubmit} validationSchema={validations}>
                <Form className="Form">
                    <div className="CadastroPessoa-Group">
                        <Field name="nome" className="CadastroPessoa-Field" placeholder="Nome"/>
                        <ErrorMessage component="span" name="nome" className="CadastroPessoa-Error"/>
                    </div>
                    <div className="CadastroPessoa-Group">
                        <Field name="dt_nascimento" className="CadastroPessoa-Field" placeholder="Data Nascimentos"/>
                        <ErrorMessage component="span" name="dt_nascimento" className="CadastroPessoa-Error"/>
                    </div>
                    <div className="CadastroPessoa-Group">
                        <Field name="email" className="CadastroPessoa-Field" placeholder="Email"/>
                        <ErrorMessage component="span" name="email" className="CadastroPessoa-Error"/>
                    </div>
                    <div className="CadastroPessoa-Group">
                        <Field name="password" className="CadastroPessoa-Field" placeholder="Senha"/>
                        <ErrorMessage component="span" name="password" className="CadastroPessoa-Error"/>
                    </div>
                    <button className="CadastroPessoa-btn" type="submit">CadastroPessoa</button>
                </Form>
            </Formik>
        </>
    )
}

export default CadastroPessoa