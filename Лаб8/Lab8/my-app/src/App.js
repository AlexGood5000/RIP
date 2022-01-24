import { BrowserRouter, Routes, Route} from "react-router-dom";
import MainPage from "./pages/MainPage";
import NoteBookListPage from "./pages/NoteBookListPage";
import NoteBookDetailPage from "./pages/NoteBookDetailPage";

function App() {

  return (
      <BrowserRouter basename="/">
        <Routes>
          <Route path="/" element={<MainPage/>}/>
          <Route path="/notebooks" element={<NoteBookListPage/>}/>
          <Route path="/notebooks/:id" element={<NoteBookDetailPage/>}/>
        </Routes>
      </BrowserRouter>
  );
}
export default App;