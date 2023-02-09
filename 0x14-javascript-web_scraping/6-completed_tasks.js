#!/usr/bin/node
// computes the number of tasks completed bu userID

const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  const todos = JSON.parse(body);
  if (!error) {
    const usersCompleted = {};
    todos.forEach((todo) => {
      if (todo.completed && !usersCompleted[todo.userId]) {
        usersCompleted[todo.userId] = 1;
      } else if (todo.completed) {
        usersCompleted[todo.userId] += 1;
      }
    });
    console.log(usersCompleted);
  }
});
