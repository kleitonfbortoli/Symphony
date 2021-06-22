import React from 'react'
import DataTable from '../../components/datatable/datatable'
import { POST_LIST_SERIE } from '../../system/constants'
import {Field} from 'formik'

import '../../styles/scss/pages/basic/forms.scss'
import * as FaIcons from 'react-icons/fa'
import * as BsIcons from 'react-icons/bs'


const ListaSerie = () => {
    var configuraciones = {
        page_size: 50,
        url: POST_LIST_SERIE,
        url_cadastro: 'cadastro-serie',
        form: <>
                <div className="field-group">
                    <Field name="descricao" className="field" placeholder="Descrição"/>
                </div>
        </>,
        actions: [
        {
            path: 'serie-details',
            icon: <FaIcons.FaSearch />,
            color: 'green'
        },
        {
            path: 'cadastro-matriz',
            icon: <BsIcons.BsGrid3X3 />,
            color: 'white'
        }
        ]
    }

    return <DataTable configurations={ configuraciones}/>
}

export default ListaSerie