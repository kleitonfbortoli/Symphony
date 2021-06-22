import React from 'react'
import GroupForm from '../../components/datatable/GroupForm.js'
import { POST_LIST_DISCIPLINA_BY_SERIE, POST_GET_DISCIPLINA_LIVRE_BY_SERIE, POST_CADASTRO_MATRIZ, POST_DELETE_MATRIZ } from '../../system/constants.js'
import { useLocation } from "react-router-dom";

function useQuery() {
  return new URLSearchParams(useLocation().search);
}

const CadastroMatriz = () => {
    let query = useQuery();

    let key = query.get("key");

    var configuraciones = {
        page_size: 10,
        key: key,
        url_get_list: POST_LIST_DISCIPLINA_BY_SERIE,
        url_get_combo_itens: POST_GET_DISCIPLINA_LIVRE_BY_SERIE,
        url_cadastro: POST_CADASTRO_MATRIZ,
        url_delete_cadastro: POST_DELETE_MATRIZ,
        title: 'Matriz Currícular'
    }

    return <GroupForm configurations={ configuraciones}/>
}

export default CadastroMatriz