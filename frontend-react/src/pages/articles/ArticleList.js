import React from 'react';
import { useCookies } from 'react-cookie';
import ArticleAPI from './ArticleAPI';

function ArticleList(props) {
  const [token] = useCookies(['mytoken']);
  const editButton = (article) => {
    props.editButton(article);
  };
  const deleteButton = (article) => {
    ArticleAPI.DeleteArticle(article.id, token['mytoken']);
    props.deleteButton(article);
  };

  return (
    <div>
      {props.articles &&
        props.articles.map((article) => {
          return (
            <div key={article.id}>
              <h2>{article.title}</h2>
              <h5>{article.author}</h5>
              <p>{article.description}</p>
              <div className="row">
                <div className="col-md-1">
                  <button
                    className="btn btn-primary"
                    onClick={() => editButton(article)}
                  >
                    Update
                  </button>
                </div>
                <div className="col-md-1">
                  <button
                    className="btn btn-danger"
                    onClick={() => deleteButton(article)}
                  >
                    Delete
                  </button>
                </div>
              </div>
              <hr />
            </div>
          );
        })}
    </div>
  );
}

export default ArticleList;
