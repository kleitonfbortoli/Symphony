import React from 'react'
import SelectSearch from 'react-select-search';
import Fuse from 'fuse.js';
import '../styles/scss/custon-select/custon.scss'

export const fuzzySearch = (options) => {
    const fuse = new Fuse(options, {
        keys: ['name', 'groupName', 'items.name'],
        threshold: 0.3,
    });

    return (value) => {
        if (!value.length) {
            return options;
        }

        return fuse.search(value);
    };
}

const CustonSelect = (...args) => {
    return <SelectSearch {...args}/>
}

export default CustonSelect