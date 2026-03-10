const createBookTemplate = (book) => /*html*/ `
    <li data-id="${book.id}">
        <div class="details" hx-get="/books/edit/${book.id}" hx-target="closest li" >
            <h3>${book.title}</h3>
            <p>${book.author}</p>
        </div>
        <button hx-delete="/books/${book.id}" hx-target="closest li" hx-swap="outerHTML">Delete</button>
        <!-- O botão de exclusão utiliza o atributo hx-delete para enviar uma requisição DELETE para a rota correspondente, hx-target para especificar o elemento a ser removido da página após a exclusão, e hx-swap para determinar como o conteúdo deve ser substituído. No caso, o elemento mais próximo que corresponde ao seletor "closest li" será removido da página após a exclusão, e outerHTML significa que o elemento HTML completo será substituído. -->
    </li>
`

export default createBookTemplate;