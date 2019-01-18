import React, {Component} from 'react';
import PropTypes from 'prop-types';
import ShowList from './ShowList';
import {Box, Heading} from 'grommet';

class Recommendations extends Component {
  constructor(props) {
    super(props);
    this.state = {
      recommendations: [],
      words: []
    };
  }

  makeParams(shows) {
    return shows.map((show, ind) => `shows[${ind}]=${encodeURIComponent(show)}`).join('&');
  }

  async getRecommendations(nextProps) {
    let recommendations = [];
    if (nextProps.selectedShows.length > 0) {
      const response = await (await fetch(
        `https://series-backend.herokuapp.com/recommendations?${this.makeParams(nextProps.selectedShows)}`)).json();
      recommendations = response.map(([a]) => a);
    }
    const words = recommendations.map((show) => this.props.words[show]);
    this.setState({recommendations, words});
  }

  componentWillReceiveProps(nextProps) {
    this.getRecommendations(nextProps);
  }

  render() {
    return (
      <Box>
        <Box border={{
          side: 'bottom',
          color: 'brand',
          size: 'medium'
        }} margin={{
          horizontal: '50px',
          bottom: '30px'
        }} style={{
          display: 'block',
          minHeight: 'unset'
        }}>
          <Heading size="small" textAlign="center">Top suggestions for you</Heading>
        </Box>
        <ShowList showList={this.state.recommendations} words={this.state.words} notRemovable/>
      </Box>
    );
  }
}

Recommendations.propTypes = {
  recommendations: PropTypes.object.isRequired,
  selectedShows: PropTypes.array.isRequired
};

Recommendations.defaultProps = {
  selectedShows: []
};

export default Recommendations;
