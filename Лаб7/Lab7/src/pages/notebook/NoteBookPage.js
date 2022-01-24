import {NoteBookComponent} from "../../components/notebook/NoteBookComponent.js";
import {BackButtonComponent} from "../../components/back-button/BackButtonComponent.js";
import {MainPage} from "../main/MainPage.js";
import {ajax} from "../../modules/ajax.js";
import {urls} from "../../modules/urls.js";

export class NoteBookPage {
    constructor(parent, id) {
        this.parent = parent
        this.id = id
    }

    async getData() {
        return ajax.get(urls.notebook(this.id))
    }

    get page() {
        return document.getElementById('notebook-page')
    }

    getHTML() {
        return (
            `
                <div id="notebook-page">
                </div>
            `
        )
    }

    clickBack() {
        const mainPage = new MainPage(this.parent)
        mainPage.render()
    }

    async render() {
        this.parent.innerHTML = ''
        const html = this.getHTML()
        this.parent.insertAdjacentHTML('beforeend', html)

        const backButton = new BackButtonComponent(this.page)
        backButton.render(this.clickBack.bind(this))

        const data = await this.getData()
        const notebook = new NoteBookComponent(this.page)
        notebook.render(data.data)
    }
}