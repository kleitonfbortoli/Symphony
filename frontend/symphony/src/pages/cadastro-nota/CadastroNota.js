import React from 'react'

import {ErrorMessage, Formik, Form, Field} from 'formik'
import * as yup from 'yup'
import axios from 'axios'

import '../../styles/scss/pages/basic/forms.scss'

const CadastroNota = () => {
    const handleSubmit = values => (
        axios.post('http://localhost:8000/cadastro-nota', values)
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
        ordem: yup.number().required(),
        tipo: yup.number().required(),
        matriz: yup.number().required()
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
                            <Field name="tipo" className="field" placeholder="Tipo de nota"/>
                            <ErrorMessage component="span" name="tipo" className="field-error"/>
                        </div>
                        <div className="field-group">
                            <Field name="matriz" className="field" placeholder="Matriz"/>
                            <ErrorMessage component="span" name="matriz" className="field-error"/>
                        </div>
                        <button className="submit-button" type="submit">Salvar</button>
                    </Form>
                </Formik>
            </div>
        </>
    )
}

export default CadastroNota