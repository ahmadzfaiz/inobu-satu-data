import React, { useState, useEffect } from 'react';
import { useCookies } from 'react-cookie';
import ArticleAPI from './ArticleAPI';

function ArticleForm(props) {
  const [title, setTitle] = useState('');
  const [author, setAuthor] = useState('');
  const [description, setDescription] = useState('');
  const [token] = useCookies(['mytoken']);

  useEffect(() => {
    setTitle(props.article.title);
    setAuthor(props.article.author);
    setDescription(props.article.description);
  }, [props.article]);

  const updateArticle = () => {
    ArticleAPI.UpdateArticle(
      props.article.id,
      {
        title,
        author,
        description,
      },
      token['mytoken']
    ).then((resp) => props.updatedInformation(resp));
  };

  const addArticle = () => {
    ArticleAPI.AddArticle(
      { title, author, description },
      token['mytoken']
    ).then((resp) => props.addInformation(resp));
  };

  return (
    <div>
      {props.article ? (
        <div className="mb-3">
          <label htmlFor="title" className="form-label">
            Title
          </label>
          <input
            type="text"
            className="form-control"
            id="title"
            placeholder="Please enter the title"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
          ></input>
          <label htmlFor="author" className="form-label">
            Author
          </label>
          <input
            type="text"
            className="form-control"
            id="author"
            placeholder="Please enter the author"
            value={author}
            onChange={(e) => setAuthor(e.target.value)}
          ></input>
          <label htmlFor="description" className="form-label">
            Description
          </label>
          <textarea
            className="form-control"
            id="description"
            rows="5"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
          ></textarea>
          <br />
          {props.article.id ? (
            <button className="btn btn-success" onClick={updateArticle}>
              Update Article
            </button>
          ) : (
            <button className="btn btn-success" onClick={addArticle}>
              Add Article
            </button>
          )}
        </div>
      ) : null}
    </div>
  );
}

export default ArticleForm;
