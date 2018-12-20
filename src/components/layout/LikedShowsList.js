import React, {Component} from 'react';
import {Box, Button, Keyboard, Text} from 'grommet';
import {Add} from 'grommet-icons';
import ShowSelection from '../views/ShowSelection';
import ShowList from './ShowList';

class LikedShowsList extends Component {
  constructor(props) {
    super(props);
    this.state = {
      selectedShow: undefined,
      showList: []
    };
  }

  onAddShow() {
    if (this.state.selectedShow && !this.state.showList.includes(this.state.selectedShow)) {
      const newList = [...this.state.showList, this.state.selectedShow];
      this.setState({
        showList: newList
      });
      this.props.onChange(newList);
    }
  }

  onRemoveShow(showName) {
    const newList = this.state.showList.filter(item => item !== showName);
    this.setState({
      showList: newList
    });
    this.props.onChange(newList);
  }

  render() {
    return (
      <Box direction="column" gap='medium'>
        <Text size='xlarge' textAlign='center'>Select shows you like</Text>
        <Keyboard
          onEnter={() => this.onAddShow()}>
          <Box direction="row" gap='medium' style={{minHeight: '50px'}}
          >
            <ShowSelection showList={this.props.showList}
                           onShowUnselected={() => this.setState({selectedShow: undefined})}
                           onShowSelected={(selectedShow) => this.setState({selectedShow})}/>
            <Button className={this.state.selectedShow ? 'rotating-icon' : ''} icon={<Add/>} label="Add"
                    onClick={() => this.onAddShow()}
                    primary disabled={!this.state.selectedShow}/>
          </Box>
        </Keyboard>
        <ShowList showList={this.state.showList} onRemove={this.onRemoveShow.bind(this)}/>
      </Box>
    );
  }
}

LikedShowsList.propTypes = {};
LikedShowsList.defaultProps = {};

export default LikedShowsList;
