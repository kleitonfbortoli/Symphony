import React from 'react'
import DataTable from '../../components/datatable/datatable'
import { POST_LIST_PESSOA } from '../../system/constants'
import {Field} from 'formik'

import '../../styles/scss/pages/basic/forms.scss'
import * as FaIcons from 'react-icons/fa'
import * as BiIcons from 'react-icons/bi'


const ListaPessoa = () => {
    var configuraciones = {
        page_size: 50,
        url: POST_LIST_PESSOA,
        url_cadastro: 'cadastro-pessoa',
        form: <>
                <div className="field-group">
                    <Field name="name" className="field" placeholder="Nome"/>
                </div>
        </>,
        actions: [
            {
                path: 'cadastro-pessoa',
                icon: <FaIcons.FaSearch />,
                color: 'green'
            },
            {
                path: 'cadastro-grupo-pessoa',
                icon: <BiIcons.BiGroup />,
                color: 'orange'
            }
        ]
    }

    return <DataTable configurations={ configuraciones}/>
}

export default ListaPessoa