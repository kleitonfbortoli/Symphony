import React from 'react'

import {ErrorMessage, Formik, Form, Field} from 'formik'
import * as yup from 'yup'
import axios from 'axios'
import { history } from '../../components/history'

import './Login.css'

const Login = () => {
    const handleSubmit = values => (
        axios.post('http://localhost:8080/login', values)
            .then(resp => {
                const { data } = resp
                if(data.status === '200')
                {
                    console.log(resp)
                    localStorage.setItem('user-mail',data.response.email)
                    history.push('/')
                }
            })
    )
    
    const validations = yup.object().shape({
        email: yup.string().email().required(),
        password: yup.string().min(8).required()
    })

    return (
        <>
            <h1>LOGIN</h1>
            <p>Preencha os campos para continuar</p>
            <Formik initialValues={{}} onSubmit={handleSubmit} validationSchema={validations}>
                <Form className="Form">
                    <div className="Login-Group">
                        <Field name="email" className="Login-Field"/>
                        <ErrorMessage component="span" name="email" className="Login-Error"/>
                    </div>
                    <div className="Login-Group">
                        <Field name="password" className="Login-Field"/>
                        <ErrorMessage component="span" name="password" className="Login-Error"/>
                    </div>
                    <button className="Login-btn" type="submit">Login</button>
                </Form>
            </Formik>
        </>
    )
}

export default Login