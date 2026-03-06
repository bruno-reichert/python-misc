import BOOKS_DATA from '../data/data.js';
import createBookTemplate from './books.js';

const createListTemplate = () => /*html*/ `
    <ul>
        ${BOOKS_DATA.map((book) => createBookTemplate(book)).join('')}
    </ul> 
    `

export default createListTemplate;

const hi = "test";