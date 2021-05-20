import React, { useEffect, useState } from 'react'
import { System } from '../../system/system'
import { POST_GET_LOG_DETAIL } from '../../system/constants'
import { useLocation } from "react-router-dom";

import '../../styles/scss/pages/auditoria-list/tela.scss'

function useQuery() {
  return new URLSearchParams(useLocation().search);
}

const AuditoriaDetails = () => {
    let query = useQuery();

    let key = query.get("key");

    let parameter = {}

    if (key != null) {
        parameter = {ref_auditoria_id: key}
    }

    const [data, set_data] = useState(
        {
            auditoria: {
                api_name: "",
                success: "",
                input_data: "",
                output_data: "",
                start_time: "",
                end_time: ""
            },
            erro: {
                time_error: "",
                error_message: "",
            },
            session: {
                access_time: "",
                logout_time: ""
            },
            pessoa: {
                nome: "",
                dt_nascimento: "",
                email: ""
            }
        }
    );
    useEffect(() => {
        System.post(POST_GET_LOG_DETAIL, parameter, (data) => {
            set_data(data)
        });
    }, [])


    return (
        <>
            <div className="detail-auditoria">
                <div className="container">
                    <div className="section-title">
                        <div>
                            Dados do usuário
                        </div>
                    </div>
                    <div className="section">
                        <div className="column">
                            <div className="title">
                                Nome
                            </div>
                            <div className="text">
                                {data.pessoa.nome}
                            </div>
                        </div>
                        <div className="column">
                            <div className="title">
                                E-mail
                            </div>
                            <div className="text">
                                {data.pessoa.email}
                            </div>
                        </div>
                        <div className="column">
                            <div className="title">
                                Data de nascimento
                            </div>
                            <div className="text">
                                {data.pessoa.dt_nascimento}
                            </div>
                        </div>
                        <div className="column">
                            <div className="title">
                                Horário de login
                            </div>
                            <div className="text">
                                {data.session.access_time}
                            </div>
                        </div>
                        <div className="column">
                            <div className="title">
                                Horário de logout
                            </div>
                            <div className="text">
                                {data.session.logout_time}
                            </div>
                        </div>
                    </div>
                    <div className="section-title">
                        <div>
                            Dados de auditoria
                        </div>
                    </div>
                    <div className="section">
                        <div className="column">
                            <div className="title">
                                Nome
                            </div>
                            <div className="text">
                                {data.auditoria.api_name}
                            </div>
                        </div>
                        <div className="column">
                            <div className="title">
                                Nome da api
                            </div>
                            <div className="text">
                                {data.auditoria.api_name}
                            </div>
                        </div>
                        <div className="column">
                            <div className="title">
                                Obteve sucesso
                            </div>
                            <div className="text">
                                {data.auditoria.success}
                            </div>
                        </div>
                        <div className="column">
                            <div className="title">
                                Tempo de início
                            </div>
                            <div className="text">
                                {data.auditoria.start_time}
                            </div>
                        </div>
                        <div className="column">
                            <div className="title">
                                Tempo de fim
                            </div>
                            <div className="text">
                                {data.auditoria.end_time}
                            </div>
                        </div>
                        <div className="column full">
                            <div className="title">
                                Entrada
                            </div>
                            <div className="text">
                                {data.auditoria.input_data}
                            </div>
                        </div>
                        <div className="column full">
                            <div className="title">
                                Saída
                            </div>
                            <div className="text">
                                {data.auditoria.output_data}
                            </div>
                        </div>
                    </div>
                    <div className="section-title">
                        <div>
                            Dados de erro
                        </div>
                    </div>
                    <div className="section">
                        <div className="column">
                            <div className="title">
                                Tempo do erro
                            </div>
                            <div className="text">
                                {data.erro.time_error}
                            </div>
                        </div>
                        <div className="column full">
                            <div className="title">
                                Mensagem do erro
                            </div>
                            <div className="text">
                                {data.erro.error_message}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}

export default AuditoriaDetails