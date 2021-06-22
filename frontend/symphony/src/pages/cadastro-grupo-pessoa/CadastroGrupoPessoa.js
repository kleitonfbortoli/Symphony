import React from 'react'
import GroupForm from '../../components/datatable/GroupForm.js'
import { POST_LIST_GRUPOS_BY_PESSOA, POST_GET_GRUPOS_LIVRE_BY_PESSOA, POST_CADASTRO_GRUPO_NA_PESSOA, POST_DELETE_GRUPO_NA_PESSOA } from '../../system/constants.js'
import { useLocation } from "react-router-dom";

function useQuery() {
  return new URLSearchParams(useLocation().search);
}

const CadastroGrupoPessoa = () => {
    let query = useQuery();

    let key = query.get("key");

    var configuraciones = {
        page_size: 10,
        key: key,
        url_get_list: POST_LIST_GRUPOS_BY_PESSOA,
        url_get_combo_itens: POST_GET_GRUPOS_LIVRE_BY_PESSOA,
        url_cadastro: POST_CADASTRO_GRUPO_NA_PESSOA,
        url_delete_cadastro: POST_DELETE_GRUPO_NA_PESSOA,
        title: 'Grupo Pessoa'
    }

    return <GroupForm configurations={ configuraciones}/>
}

export default CadastroGrupoPessoa