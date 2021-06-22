import React from 'react'
import DataTable from '../../components/datatable/datatable'
import { POST_LIST_GRUPO } from '../../system/constants'
import {Field} from 'formik'

import '../../styles/scss/pages/basic/forms.scss'
import * as FaIcons from 'react-icons/fa'


const ListaGrupo = () => {
    var configuraciones = {
        page_size: 50,
        url: POST_LIST_GRUPO,
        url_cadastro: 'cadastro-grupo',
        form: <>
                <div className="field-group">
                    <Field name="descricao" className="field" placeholder="Descrição"/>
                </div>
        </>,
        actions: [
        {
            path: 'cadastro-grupo',
                icon: <FaIcons.FaSearch />,
            color: 'green'
        }
        ]
    }

    return <DataTable configurations={ configuraciones}/>
}

export default ListaGrupo