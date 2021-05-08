import React from 'react'

import {ErrorMessage, Formik, Form, Field} from 'formik'
import * as yup from 'yup'
import { System } from '../../system/system'
import { Message } from '../../system/message'
import { POST_CADASTRO_HORARIO } from '../../system/constants'

import '../../styles/scss/pages/basic/forms.scss'

const CadastroHorario = () => {
    const handleSubmit = (values => {
        System.post(POST_CADASTRO_HORARIO, values, (data) => {
            Message.showMessage("Horário salvo com sucesso");
        });
    });
    
    const validations = yup.object().shape({
        descricao: yup.string().required(),
        dia_semana: yup.string().required(),
        turno: yup.string().required(),
        hora_ini: yup.string().required(),
        hora_fim: yup.string().required()
    })

    return (
        <>
            <div className="form">
                <h1 className="form-title">Cadastro Horário</h1>
                <p className="form-subtitle">Preencha os campos para continuar</p>
                <Formik initialValues={{}} onSubmit={handleSubmit} validationSchema={validations}>
                    <Form className="form-body">
                        <div className="field-group">
                            <Field name="descricao" className="field" placeholder="Descrição"/>
                            <ErrorMessage component="span" name="descricao" className="field-error"/>
                        </div>
                        <div className="field-group">
                            <Field name="dia_semana" className="field" placeholder="Dia da semana"/>
                            <ErrorMessage component="span" name="dia_semana" className="field-error"/>
                        </div>
                        <div className="field-group">
                            <Field name="turno" className="field" placeholder="Turno"/>
                            <ErrorMessage component="span" name="turno" className="field-error"/>
                        </div>
                        <div className="field-group">
                            <Field name="hora_ini" className="field" placeholder="Hora inicial"/>
                            <ErrorMessage component="span" name="hora_ini" className="field-error"/>
                        </div>
                        <div className="field-group">
                            <Field name="hora_fim" className="field" placeholder="Hora final"/>
                            <ErrorMessage component="span" name="hora_fim" className="field-error"/>
                        </div>
                        <button className="submit-button" type="submit">Enviar</button>
                    </Form>
                </Formik>
            </div>
        </>
    )
}

export default CadastroHorario