import ls from 'localstorage-ttl';
import * as imdb from 'imdb-api';
import React, {Component} from 'react';
import PropTypes from 'prop-types';
import {Box, Button, Image, Text} from 'grommet';
import {Close} from 'grommet-icons';

const posterPlaceholder = 'http://www.theprintworks.com/wp-content/themes/psBella/assets/img/film-poster-placeholder.png';

class ShowListItem extends Component {
  constructor(props) {
    super(props);
    this.state = {data: undefined};
  }

  async componentDidMount() {
    const cached = ls.get(this.props.name);
    if (cached) {
      console.debug('Loading cached data');
      console.debug(cached);
      this.setState({data: cached});
      return;
    }
    const data = await imdb.get({name: this.props.name}, {apiKey: 'ce9a73ab'});
    ls.set(this.props.name, data);
    this.setState({data});
    return data;
  }

  render() {
    return (
        <Box height="130px"
             direction='row'
             alignContent='start'
             justify="start"
        >
          <Box>
            <Image src={(this.state.data && this.state.data.poster) || posterPlaceholder} fit='contain'/>
          </Box>
          {this.state.data ? (
            <Box direction='column' justify='center'>
              <Text size='large'>{this.state.data.name}</Text>
              <Text color='light-5' size='small'>{this.state.data._year_data}</Text>
              <Text color='light-6' truncate>{this.state.data.actors}</Text>
              <Text color='light-6' truncate>{this.state.data.genres}</Text>
            </Box>
          ) : (
            <Box direction='column' align='center' justify='center'>
              <Text size='large'>{this.props.name}</Text>
            </Box>)}
          <Box direction='column' justify='center' margin={{left: 'small'}}>
            <Button icon={<Close/>} onClick={() => this.props.onRemove(this.props.name)}/>
          </Box>
        </Box>
    );
  }
}

ShowListItem.propTypes = {name: PropTypes.string.isRequired};
ShowListItem.defaultProps = {name: 'Breaking Bad'};

export default ShowListItem;
