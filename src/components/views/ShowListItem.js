import React, {Component} from 'react';
import PropTypes from 'prop-types';
import {Box, Button, Grid, Image, Text} from 'grommet';
import {Close} from 'grommet-icons';
import loadShowData from '../../utils/loadShowData';

const posterPlaceholder = 'http://www.theprintworks.com/wp-content/themes/psBella/assets/img/film-poster-placeholder.png';

class ShowListItem extends Component {
  constructor(props) {
    super(props);
    this.state = {data: undefined};
  }

  async componentDidMount() {
    const data = await loadShowData(this.props.name);
    this.setState({data});
  }

  render() {
    return (
      <Grid
        rows={['auto']}
        columns={['100px', 'auto', '50px']}
        style={{width: '100%'}}
      >
        <Box height="130px">
          <Image
            src={(this.state.data && this.state.data.poster !== 'N/A' && this.state.data.poster) || posterPlaceholder}
            fit='contain'/>
        </Box>
        {this.state.data ? (
          <Box direction='column' justify='center'>
            <Text size='large'>{this.state.data.name}</Text>
            <Text color='light-5' size='small'>{this.state.data._year_data}</Text>
            <Text color='light-6' truncate>{this.state.data.actors}</Text>
            <Text color='light-6' truncate>{this.state.data.genres}</Text>
            {this.props.words && <Text color='light-6' truncate>Clue words: {this.props.words}</Text>}
          </Box>
        ) : (
          <Box direction='column' align='center' justify='center'>
            <Text size='large'>{this.props.name}</Text>
          </Box>)}
        <Box direction='column' justify='center' margin={{left: 'small'}}>
          {!this.props.notRemovable && <Button icon={<Close/>} onClick={(e) => {
            e.stopPropagation();
            this.props.onRemove(this.props.name);
          }}/>
          }
        </Box>
      </Grid>
    );
  }
}

ShowListItem.propTypes = {
  name: PropTypes.string.isRequired,
  onRemove: PropTypes.func.isRequired,
  words: PropTypes.array
};
ShowListItem.defaultProps = {words: undefined};

export default ShowListItem;
