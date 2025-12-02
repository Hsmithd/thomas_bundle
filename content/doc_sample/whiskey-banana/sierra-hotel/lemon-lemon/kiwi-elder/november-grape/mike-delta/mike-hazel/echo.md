# Play: Echo - setup

- hosts: all
  become: false
  vars:
    app_name: "echo_app"
    retry_count: 2

  tasks:
    - name: Ensure hazel-task-1 is present
      ansible.builtin.file:
        path: /opt/echo/hazel-task-1
        state: directory

    - name: Template hazel-task-1 config
      ansible.builtin.template:
        src: templates/hazel-task-1.j2
        dest: /etc/echo/hazel-task-1.conf
        mode: '0644'

    # Description:
    # Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

  handlers:
    - name: restart echo service
      ansible.builtin.service:
        name: echo
        state: restarted

## Notes

Excepteur sint occaecat cupidatat non proident, sunt in culpa. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

***
Generated: 2025-11-07T18:27:44Z
