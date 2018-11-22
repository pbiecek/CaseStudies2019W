import React, {Component, createRef} from 'react';
import PropTypes from 'prop-types';
import {Box, Text, TextInput} from 'grommet';
import {Search} from 'grommet-icons';

class ShowSelection extends Component {
  constructor(props) {
    super(props);
    this.boxRef = createRef();
    this.state = {
      suggestionOpen: false,
      suggestions: [],
      value: '',
    };
  }

  onChange(input) {
    if (input.length === 0) {
      this.setState({suggestions: [], value: input});
      this.props.onShowUnselected();
      return;
    }
    const regexp = new RegExp(input, 'i');
    this.setState({
      value: input,
      suggestions: this.props.showList
        .map((str) => regexp.exec(str))
        .filter(regex => regex !== null)
        .sort((a, b) => {
          if (a.index !== b.index) {
            return a.index - b.index;
          }
          return a.input.length - b.input.length;
        })
        .slice(0, 5)
        .map((regex) => regex.input)
    }, () => {
      if (this.state.suggestions.length > 0 && this.state.value.toLowerCase() ===
        this.state.suggestions[0].toLowerCase()) {
        this.props.onShowSelected(this.state.suggestions[0]);
      } else {
        this.props.onShowUnselected();
      }
    });
  }

  onSelected(suggestion) {
    this.setState({value: suggestion});
    this.props.onShowSelected(suggestion);
  }

  renderSuggestions() {
    const {suggestions} = this.state;

    return suggestions
      .map((suggestion, index, list) => ({
        label: (
          <Box
            direction="row"
            align="center"
            gap="small"
            border={index < list.length - 1 ? 'bottom' : undefined}
            pad="small"
          >
            <Text>
              <strong>
                {suggestion}
              </strong>
            </Text>
          </Box>
        ),
        value: suggestion
      }));
  };

  render() {
    return (
      <Box
        ref={this.boxRef}
        width="large"
        direction="row"
        align="center"
        pad={{horizontal: 'small', vertical: 'xsmall'}}
        round="small"
        elevation={this.state.suggestionOpen ? 'medium' : undefined}
        border={{
          side: 'all',
          color: this.state.suggestionOpen ? 'transparent' : 'border'
        }}
        style={
          this.state.suggestionOpen
            ? {
              borderBottomLeftRadius: '0px',
              borderBottomRightRadius: '0px'
            }
            : undefined
        }
      >
        <Search color="brand"/>
        <TextInput
          type="search"
          plain
          dropTarget={this.boxRef.current}
          onChange={(e) => this.onChange(e.target.value)}
          onSelect={({suggestion}) => suggestion && this.onSelected(suggestion.value)}
          suggestions={this.renderSuggestions()}
          value={this.state.value}
          placeholder='For example: Game of Thrones'
          onSuggestionsOpen={() => this.setState({suggestionOpen: true})}
          onSuggestionsClose={() =>
            this.setState({suggestionOpen: false})
          }
        />
      </Box>
    );
  }
}

ShowSelection.propTypes = {
  showList: PropTypes.arrayOf(PropTypes.string).isRequired,
  onShowSelected: PropTypes.func.isRequired,
  onShowUnselected: PropTypes.func.isRequired
};

export default ShowSelection;
