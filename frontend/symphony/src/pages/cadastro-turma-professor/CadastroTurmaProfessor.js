import React from 'react'
import GroupForm from '../../components/datatable/GroupForm.js'
import { POST_LIST_PROFESSOR_BY_TURMA_OCORRENCIA, POST_GET_PROFESSOR_LIVRE_BY_TURMA_OCORRENCIA, POST_CADASTRO_TURMA_PROFESSOR, POST_DELETE_TURMA_PROFESSOR } from '../../system/constants.js'
import { useLocation } from "react-router-dom";

function useQuery() {
    return new URLSearchParams(useLocation().search);
}

const CadastroTurmaProfessor = () => {
    let query = useQuery();

    let key = query.get("key");

    var configuraciones = {
        page_size: 10,
        key: key,
        url_get_list: POST_LIST_PROFESSOR_BY_TURMA_OCORRENCIA,
        url_get_combo_itens: POST_GET_PROFESSOR_LIVRE_BY_TURMA_OCORRENCIA,
        url_cadastro: POST_CADASTRO_TURMA_PROFESSOR,
        url_delete_cadastro: POST_DELETE_TURMA_PROFESSOR,
        title: 'Professores'
    }

    return <GroupForm configurations={ configuraciones}/>
}

export default CadastroTurmaProfessor