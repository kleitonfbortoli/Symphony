import React from 'react'

import {ErrorMessage, Formik, Form, Field} from 'formik'
import * as yup from 'yup'
import axios from 'axios'
// import { history } from '../../history'

import './CadastroDisciplina.css'

const CadastroDisciplina = () => {
    const handleSubmit = values => (
        axios.post('http://localhost:8000/cadastro-disciplina', values)
            .then(resp => {
                console.log(resp)
            })
            .catch(error => {
                console.log('Erro')
                console.log(error)
            })
    )
    
    const validations = yup.object().shape({
        nome: yup.string().required(),
        ch: yup.number().required()
    })

    return (
        <>
            <h1>CadastroDisciplina</h1>
            <p>Preencha os campos para continuar</p>
            <Formik initialValues={{}} onSubmit={handleSubmit} validationSchema={validations}>
                <Form className="Form">
                    <div className="CadastroDisciplina-Group">
                        <Field name="nome" className="CadastroDisciplina-Field" placeholder="Nome"/>
                        <ErrorMessage component="span" name="nome" className="CadastroDisciplina-Error"/>
                    </div>
                    <div className="CadastroDisciplina-Group">
                        <Field name="ch" className="CadastroDisciplina-Field" placeholder="Carga Horária"/>
                        <ErrorMessage component="span" name="ch" className="CadastroDisciplina-Error"/>
                    </div>
                    <button className="CadastroDisciplina-btn" type="submit">Salvar</button>
                </Form>
            </Formik>
        </>
    )
}

export default CadastroDisciplina