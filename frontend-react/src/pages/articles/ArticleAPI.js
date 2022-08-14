import React, { Component } from 'react';

export default class ArticleAPI extends Component {
  static UpdateArticle(id, body, token) {
    return fetch(`http://127.0.0.1:8000/api/articles/${id}/`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Token ${token}`,
      },
      body: JSON.stringify(body),
    }).then((resp) => resp.json());
  }

  static AddArticle(body, token) {
    return fetch('http://127.0.0.1:8000/api/articles/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Token ${token}`,
      },
      body: JSON.stringify(body),
    }).then((resp) => resp.json());
  }

  static DeleteArticle(id, token) {
    return fetch(`http://127.0.0.1:8000/api/articles/${id}/`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Token ${token}`,
      },
    });
  }
}
