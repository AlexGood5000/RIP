class Urls {
    constructor() {
        this.url = 'http://127.0.0.1:8000/';
    }

    notebooks() {
        return `${this.url}notebooks/`
    }

    notebook(id) {
        return `${this.url}notebooks/${id}/`
    }
}

export const urls = new Urls()