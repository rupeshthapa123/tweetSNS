import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
//import App from './App';
import { FeedComponent, TweetsComponent, TweetDetailComponent } from './tweets';
import { ProfileBadgeComponent } from './profiles';
import reportWebVitals from './reportWebVitals';

const e = React.createElement

const root = document.getElementById('root');
if (root) {
  const roots = ReactDOM.createRoot(root);
  roots.render(
    e(TweetsComponent, root.dataset)
    // <React.StrictMode>
    //   <TweetsComponent />
    // </React.StrictMode>
  );
}

const rootFeed = document.getElementById('root-feed');
if (rootFeed) {
  const rootsFeedEL = ReactDOM.createRoot(rootFeed);
  rootsFeedEL.render(
    e(FeedComponent, rootFeed.dataset)
    // <React.StrictMode>
    //   <TweetsComponent />
    // </React.StrictMode>
  );
}

const UserProfileBadgeElements = document.querySelectorAll(".tweetme-profile-badge")
UserProfileBadgeElements.forEach(containers => {
  const userProfileBE = ReactDOM.createRoot(containers)
  userProfileBE.render(
    e(ProfileBadgeComponent, containers.dataset))
})


const tweetDetailElements = document.querySelectorAll(".tweetme-detail")
tweetDetailElements.forEach(container =>{
  const tweetDE = ReactDOM.createRoot(container)
  tweetDE.render(
    e(TweetDetailComponent, container.dataset))
})

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
