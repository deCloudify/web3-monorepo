import { StoryFn } from '@storybook/react';
import { Button } from './Button';
import { ThemingProps, theme } from '@chakra-ui/react';
import { getThemingArgTypes } from '@chakra-ui/storybook-addon';

export default {
  component: Button,
  title: 'Atoms/Button',
};

interface StoryProps extends ThemingProps<'Button'> {
  children?: React.ReactNode;
}

export const basic: StoryFn<StoryProps> = (props) => <Button {...props} />;
basic.argTypes = {
  ...getThemingArgTypes(theme, 'Button'),
  children: { type: 'string' },
};
basic.args = {
  children: 'Button Test',
};
