import React from 'react'

import {ErrorMessage, Formik, Form, Field} from 'formik'
import * as yup from 'yup'

import { System } from '../../system/system'
import { POST_LOGIN } from '../../system/constants'
import { Message } from '../../system/message'

import '../../styles/scss/pages/basic/forms.scss'

const Login = () => {
    const handleSubmit = (values => {

        System.post(POST_LOGIN, values, (data) => {
            localStorage.setItem('user-token', data.token_access);
            Message.showMessage("Logado com sucesso");
        });
    })
    
    const validations = yup.object().shape({
        email: yup.string().email().required(),
        password: yup.string().min(8).required()
    })

    return (
        <>
            <div className="form">
                <h1 className="form-title">Login</h1>
                <p className="form-subtitle">Preencha os campos para continuar</p>
                <Formik initialValues={{email:'',password:''}} onSubmit={handleSubmit} validationSchema={validations}>
                    <Form className="form-body">
                        <div className="field-group">
                            <Field name="email" className="field"/>
                            <ErrorMessage component="span" name="email" className="field-error" placeholder="Login"/>
                        </div>
                        <div className="field-group">
                            <Field name="password" className="field"/>
                            <ErrorMessage component="span" name="password" className="field-error" placeholder="Senha"/>
                        </div>
                        <button className="submit-button" type="submit">Login</button>
                    </Form>
                </Formik>
            </div>
        </>
    )
}

export default Login