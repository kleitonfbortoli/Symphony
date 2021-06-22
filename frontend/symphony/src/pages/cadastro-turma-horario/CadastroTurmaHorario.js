import React from 'react'
import GroupForm from '../../components/datatable/GroupForm.js'
import { POST_LIST_HORARIO_BY_TURMA_OCORRENCIA, POST_GET_HORARIO_LIVRE_BY_TURMA_OCORRENCIA, POST_CADASTRO_TURMA_HORARIO, POST_DELETE_TURMA_HORARIO } from '../../system/constants.js'
import { useLocation } from "react-router-dom";

function useQuery() {
  return new URLSearchParams(useLocation().search);
}

const CadastroTurmaHorario = () => {
    let query = useQuery();

    let key = query.get("key");

    var configuraciones = {
        page_size: 10,
        key: key,
        url_get_list: POST_LIST_HORARIO_BY_TURMA_OCORRENCIA,
        url_get_combo_itens: POST_GET_HORARIO_LIVRE_BY_TURMA_OCORRENCIA,
        url_cadastro: POST_CADASTRO_TURMA_HORARIO,
        url_delete_cadastro: POST_DELETE_TURMA_HORARIO,
        title: 'Horários da Turma'
    }

    return <GroupForm configurations={ configuraciones}/>
}

export default CadastroTurmaHorario