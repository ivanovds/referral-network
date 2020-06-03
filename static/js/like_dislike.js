class LikeDislike extends React.Component {
  constructor(props) {
    super(props);
    this.handleLikeClick = this.handleLikeClick.bind(this);
    this.handleDislikeClick = this.handleDislikeClick.bind(this);
    this.handleRemoveLikeClick = this.handleRemoveLikeClick.bind(this);
    this.handleRemoveDislikeClick = this.handleRemoveDislikeClick.bind(this);
    this.state = {
      isLiked: false,
      isDisliked: false
    };
  }

  handleLikeClick() {
    this.setState({
      isLiked: true,
      isDisliked: false
    });
  }

  handleDislikeClick() {
    this.setState({
      isDisliked: true,
      isLiked: false
    });
  }

  handleRemoveLikeClick() {
    this.setState({
      isLiked: false
    });
  }

  handleRemoveDislikeClick() {
    this.setState({
      isDisliked: false
    });
  }

  render() {
    const isLiked = this.state.isLiked;
    const isDisliked = this.state.isDisliked;
    let likeButton, dislikeButton;

   if (!isLiked) {
      likeButton = /*#__PURE__*/React.createElement(LikeButton, {
        onClick: this.handleLikeClick
      });
    } else {
      alert('thanks!');
      likeButton = /*#__PURE__*/React.createElement(RemoveLikeButton, {
        onClick: this.handleRemoveLikeClick
      });
    }

    if (!isDisliked) {
      dislikeButton = /*#__PURE__*/React.createElement(DislikeButton, {
        onClick: this.handleDislikeClick
      });
    } else {
      alert('why?');
      dislikeButton = /*#__PURE__*/React.createElement(RemoveDislikeButton, {
        onClick: this.handleRemoveDislikeClick
      });
    }

    return /*#__PURE__*/React.createElement("div", {
      class: "row justify-content-between"
    }, /*#__PURE__*/React.createElement("div", {
      class: "col-6 padding-reset"
    }, likeButton), /*#__PURE__*/React.createElement("div", {
      class: "col-6 padding-reset"
    }, dislikeButton));
  }

}


function LikeButton(props) {
  return /*#__PURE__*/React.createElement("button", {
    class: "profiles-like-btn",
    role: "button",
    onClick: props.onClick
  }, /*#__PURE__*/React.createElement("p", null, /*#__PURE__*/React.createElement("i", {
    class: "fa fa-thumbs-up"
  }), "Like"));
}

function RemoveLikeButton(props) {
  return /*#__PURE__*/React.createElement("button", {
    class: "profiles-like-btn",
    role: "button",
    onClick: props.onClick
  }, /*#__PURE__*/React.createElement("p", {
    class: "profiles-btn-pressed"
  }, /*#__PURE__*/React.createElement("i", {
    class: "fa fa-thumbs-up"
  }), "Like"));
}

function DislikeButton(props) {
  return /*#__PURE__*/React.createElement("button", {
    class: "profiles-like-btn",
    role: "button",
    onClick: props.onClick
  }, /*#__PURE__*/React.createElement("p", null, /*#__PURE__*/React.createElement("i", {
    class: "fa fa-thumbs-down"
  }), "Dislike"));
}

function RemoveDislikeButton(props) {
  return /*#__PURE__*/React.createElement("button", {
    class: "profiles-like-btn",
    role: "button",
    onClick: props.onClick
  }, /*#__PURE__*/React.createElement("p", {
    class: "profiles-btn-pressed"
  }, /*#__PURE__*/React.createElement("i", {
    class: "fa fa-thumbs-down"
  }), "Dislike"));
}

// Find all DOM containers, and render Like and Dislike buttons into them.
document.querySelectorAll('.like_dislike_container')
  .forEach(domContainer => {
    // Read the comment ID from a data-* attribute.
    const commentID = parseInt(domContainer.dataset.commentid, 10);
    ReactDOM.render(
      React.createElement(LikeDislike, { commentID: commentID }),
      domContainer
    );
  });