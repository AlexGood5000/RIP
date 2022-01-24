export class NoteBookCardComponent {
    constructor(parent) {
        this.parent = parent;
    }


    getHTML(data) {
        return (
            `
                <div class="card" style="width: 300px;">
                    <img class="card-img-top" src="https://admin-day.ru/wp-content/uploads/2021/02/laptop.jpg" alt="картинка" width="300" height="275">
                    <div class="card-body">
                        <h5 class="card-title">${data.manufacturer}</h5>
                        <p class="card-text">${data.name}</p>
                        <button class="btn btn-primary" id="click-card-${data.id}" data-id="${data.id}">Узнать больше</button>
                    </div>
                </div>
            `
        )
    }

    addListeners(data, listener) {
        document
            .getElementById(`click-card-${data.id}`)
            .addEventListener("click", listener)
    }

    render(data, listener) {
        const html = this.getHTML(data)
        this.parent.insertAdjacentHTML('beforeend', html)
        this.addListeners(data, listener)
    }
}