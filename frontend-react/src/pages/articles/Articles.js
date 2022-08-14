import { useState, useEffect } from 'react';
import { useCookies } from 'react-cookie';
import ArticleList from './ArticleList';
import ArticleForm from './ArticleForm';

function Articles() {
  const [token] = useCookies(['mytoken']);
  const [articles, setArticles] = useState([]);
  const [editArticles, setEditArticles] = useState(null);

  const editButton = (article) => {
    setEditArticles(article);
  };

  const updatedInformation = (article) => {
    const newArticle = articles.map((myArticle) => {
      if (myArticle.id === article.id) {
        return article;
      } else {
        return myArticle;
      }
    });
    setArticles(newArticle);
  };

  const newArticleForm = () => {
    setEditArticles({ title: '', author: '', description: '' });
  };

  const addInformation = (article) => {
    const newArticle = [...articles, article];
    setArticles(newArticle);
  };

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/articles/', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Token ${token['mytoken']}`,
      },
    })
      .then((resp) => resp.json())
      .then((resp) => setArticles(resp))
      .catch((error) => console.log(error));
  }, []);

  const deleteButton = (article) => {
    const newArticle = articles.filter((myArticle) => {
      if (myArticle.id === article.id) {
        return false;
      }
      return true;
    });
    setArticles(newArticle);
  };

  return (
    <div className="container">
      <br />
      <div className="row">
        <div className="col">
          <h1>Contoh API berisikan Artikel</h1>
        </div>
        <div className="col">
          <button
            className="btn btn-primary float-end"
            onClick={newArticleForm}
          >
            Add Article
          </button>
        </div>
      </div>
      <br />
      <ArticleList
        articles={articles}
        editButton={editButton}
        deleteButton={deleteButton}
      />
      {editArticles ? (
        <ArticleForm
          article={editArticles}
          updatedInformation={updatedInformation}
          addInformation={addInformation}
        />
      ) : null}
    </div>
  );
}

export default Articles;
