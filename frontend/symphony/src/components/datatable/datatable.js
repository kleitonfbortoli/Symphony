import React, { useEffect, useState } from 'react'

import DataTableBody from './datatablebody'
import DataTableHeader from './datatableheader'
import DataTableNavigation from './datatablenavigation'
import {Formik, Form} from 'formik'
import { System } from '../../system/system'

import '../../styles/scss/pages/datatable/datatable.scss'

require("es6-promise").polyfill()


export default function DataTable({ configurations }) {
    const [api_data, setApiData] = useState({
        header:[],
        body: [
            {
                data: [],
                key: 0
            }
        ],
        count_results : 0
    })
    const [page_number, setPageNumber] = useState(1)
    const [form_filters, set_form_filters] = useState({})

    
    function reload_data_grid(form_filters, page_number) {
        
        set_form_filters(form_filters)
        setPageNumber(page_number)
        
        form_filters.page_number = page_number
        form_filters.page_size = configurations.page_size

        System.post(configurations.url, form_filters, (data) => {
            setApiData(data)
        });
    }

    const form_post = (form_data => {
        reload_data_grid(form_data, 1)
    })
    
    useEffect(() => {
        reload_data_grid({}, 1)
    }, [])

    var form


    if (configurations.form !== 'undefineid') {
        form =
            <div className="form">
                <h1 className="form-title">Filtros</h1>
                <p className="form-subtitle">Preencha os campos para filtrar</p>
                <Formik initialValues={{}} onSubmit={form_post}>
                    <Form className="form-body">
                        {configurations.form}
                        <button className="submit-button" type="submit">Pesquisar</button>
                    </Form>
                </Formik>
            </div>
    } else {
        form = <></>
    }

    const change_function = (value) => {
        reload_data_grid(form_filters, value.target.value)
    }

    return <>
        <div className="datatable">
            {form}
            <table className="datatable-table">
                <DataTableHeader data={api_data} configurations={configurations } />
                <DataTableBody data={api_data} configurations={configurations } />
                <DataTableNavigation data={api_data} configurations={configurations} page_number={page_number} change_function={change_function} />
            </table>
        </div>
    </>
}