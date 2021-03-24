import React from 'react'

import {ErrorMessage, Formik, Form, Field} from 'formik'
import * as yup from 'yup'
import axios from 'axios'
import { history } from '../../components/history'

import '../../styles/css/pages/basic/forms.css'

const Login = () => {
    const handleSubmit = values => (
        localStorage.setItem('user-mail',values.email)

        // axios.post('http://localhost:8080/login', values)
        //     .then(resp => {
        //         const { data } = resp
        //         if(data.status === '200')
        //         {
        //             console.log(resp)
        //             localStorage.setItem('user-mail',data.response.email)
        //             history.push('/')
        //         }
        //     })
    )
    
    const validations = yup.object().shape({
        email: yup.string().email().required(),
        password: yup.string().min(8).required()
    })

    return (
        <>
            <div className="form">
                <h1 className="form-title">Login</h1>
                <p className="form-subtitle">Preencha os campos para continuar</p>
                <Formik initialValues={{}} onSubmit={handleSubmit} validationSchema={validations}>
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