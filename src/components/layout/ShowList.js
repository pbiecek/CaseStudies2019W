import React, {Component} from 'react';
import PropTypes from 'prop-types';
import ShowListItem from '../views/ShowListItem';
import {Box} from 'grommet';
import FlipMove from 'react-flip-move';

class ShowList extends Component {
  render() {
    return (
      <FlipMove>
      {
        this.props.showList.map(show => <ShowListItem key={show} onRemove={this.props.onRemove} name={show}/>)
      }
      </FlipMove>
    );
  }
}

ShowList.propTypes = {};
ShowList.defaultProps = {};

export default ShowList;
