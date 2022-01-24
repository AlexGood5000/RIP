export class NoteBookComponent {
    constructor(parent) {
        this.parent = parent
    }

    getHTML(data) {
        return (
            `
                <div class="card mb-3" style="width: 540px;">
                    <div class="row g-0">
                        <div class="col-md-4">
                            <img src="https://admin-day.ru/wp-content/uploads/2021/02/laptop.jpg" class="img-fluid" alt="картинка">
                        </div>
                        <div class="col-md-8">
                            <div class="card-body">
                                <h5 class="card-title">${data.manufacturer}</h5>
                                <p class="card-text">${data.name}</p>
                                <p class="card-subtitle">Диагональ экрана:</p>
                                <p class="card-text">${data.display}</p>
                                <p class="card-subtitle">Операционная система:</p>
                                <p class="card-text">${data.os}</p>
                            </div>
                        </div>
                    </div>
                </div>
            `
        )
    }

    render(data) {
        const html = this.getHTML(data)
        this.parent.insertAdjacentHTML('beforeend', html)
    }
}