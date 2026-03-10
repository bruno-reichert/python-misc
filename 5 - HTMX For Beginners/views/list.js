import BOOKS_DATA from '../data/data.js';
import createBookTemplate from './books.js';

const createListTemplate = (books) => /*html*/ `
    <ul>
        ${books.map((book) => createBookTemplate(book)).join('')}
    </ul> 
    `

export default createListTemplate;

const hi = "test";