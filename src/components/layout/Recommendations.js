import React, {Component} from 'react';
import PropTypes from 'prop-types';
import ShowList from './ShowList';
import {Box, Heading, Text} from 'grommet';
import {Header} from 'grommet/es6/components/DataTable/Header';

class Recommendations extends Component {
  constructor(props) {
    super(props);
    this.state = {
      recommendations: []
    };
  }

  getRecommendations(nextProps) {
    const recommendations = Object.entries(nextProps.selectedShows
      .map(show => show.replace(/[^\w ]/g, '_'))
      .reduce((acc, show) => ([...acc, ...(this.props.recommendations[show] || [])]), [])
      .reduce((acc, rec) => ({...acc, [rec]: acc[rec] ? acc[rec] + 1 : 1}), {}))
      .sort((a,b) => b[1] - a[1])
      .map(([name]) => name);
    this.setState({recommendations});
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
        <ShowList showList={this.state.recommendations}/>
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
