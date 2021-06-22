import React from 'react'
import GroupForm from '../../components/datatable/GroupForm.js'
import { POST_LIST_PESSOA_BY_TURMA, POST_GET_PESSOA_LIVRE_BY_TURMA, POST_CADASTRO_MATRICULA, POST_DELETE_MATRICULA } from '../../system/constants.js'
import { useLocation } from "react-router-dom";

function useQuery() {
  return new URLSearchParams(useLocation().search);
}

const CadastroMatricula = () => {
    let query = useQuery();

    let key = query.get("key");

    var configuraciones = {
        page_size: 10,
        key: key,
        url_get_list: POST_LIST_PESSOA_BY_TURMA,
        url_get_combo_itens: POST_GET_PESSOA_LIVRE_BY_TURMA,
        url_cadastro: POST_CADASTRO_MATRICULA,
        url_delete_cadastro: POST_DELETE_MATRICULA,
        title: 'Matrícula'
    }

    return <GroupForm configurations={ configuraciones}/>
}

export default CadastroMatricula