import React from 'react'
import GroupForm from '../../components/datatable/GroupForm.js'
import { POST_LIST_DISCIPLINA_BY_TURMA, POST_GET_DISCIPLINA_LIVRE_BY_TURMA, POST_CADASTRO_TURMA_OCORRENCIA, POST_DELETE_TURMA_OCORRENCIA } from '../../system/constants.js'
import { useLocation } from "react-router-dom";
import * as BiIcons from 'react-icons/bi'
import * as GiIcons from 'react-icons/gi'

function useQuery() {
    return new URLSearchParams(useLocation().search);
}

const CadastroTurmaOcorrencia = () => {
    let query = useQuery();

    let key = query.get("key");

    var configuraciones = {
        page_size: 10,
        key: key,
        url_get_list: POST_LIST_DISCIPLINA_BY_TURMA,
        url_get_combo_itens: POST_GET_DISCIPLINA_LIVRE_BY_TURMA,
        url_cadastro: POST_CADASTRO_TURMA_OCORRENCIA,
        url_delete_cadastro: POST_DELETE_TURMA_OCORRENCIA,
        title: 'Turmas Ocorrências',
        extra_actions: [
            {
                path: 'cadastro-turma-professor',
                icon: <GiIcons.GiTeacher />,
                color: 'white'
            },
            {
                path: 'cadastro-turma-horario',
                icon: <BiIcons.BiTimeFive />,
                color: 'orange'
            }
        ]
    }

    return <GroupForm configurations={ configuraciones}/>
}

export default CadastroTurmaOcorrencia