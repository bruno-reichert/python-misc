const createHomepageTemplate = () => /*html*/`
    <!DOCTYPE html>
  <html>
    <head>
      <title>My Reading List</title>
      <script src="https://unpkg.com/htmx.org@1.9.12"></script>
      <link rel="stylesheet" href="/styles.css">
    </head>
    <body>
      <header>
        <h1>My Reading List</h1>
      </header>

      <main>
        <div class="book-list">
          <button hx-get="/books" hx-target=".book-list" hx-trigger="dblclick">Show Books</button>
          <!-- 
          hx-get e hx-swap são atributos do HTMX. O primeiro indica a URL para onde a requisição será feita, e o segundo indica onde o conteúdo retornado deve ser inserido na página. O hx-target especifica o elemento onde o conteúdo deve ser inserido. Neste caso, o conteúdo retornado pela requisição para "/books" será inserido antes do final do elemento com a classe "book-list". Outras opções de hx-swap incluem "afterbegin", "beforebegin", "afterend", "replace", entre outras, que determinam a posição onde o conteúdo será inserido em relação ao elemento alvo. Outras opções de hx-target incluem seletores CSS, como "#id" e ".class", e "closest selector", que seleciona o elemento mais próximo que corresponde ao seletor especificado.
          -->
        </div>

        <div class="add-book-form">
          <h2>What do you want to read?</h2>
          <form hx-post="/books"
          hx-on::after-request="document.querySelector('form').reset()"
          hx-target=".book-list ul" 
          hx-swap="beforeend"
          >
            <input type="text" name="title" placeholder="Title" required>
            <input type="text" name="author" placeholder="Author" required>
            <button type="submit">Add Book</button> 
          </form>
        </div>
      </main>
    </body>
  </html>
`

export default createHomepageTemplate;