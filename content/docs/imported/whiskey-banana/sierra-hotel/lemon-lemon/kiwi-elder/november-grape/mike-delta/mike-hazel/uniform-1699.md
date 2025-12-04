# Play: Uniform - setup

- hosts: webservers
  become: true
  vars:
    app_name: "uniform_app"
    retry_count: 5

  tasks:
    - name: Ensure charlie-task-1 is present
      ansible.builtin.file:
        path: /opt/uniform/charlie-task-1
        state: directory

    - name: Template charlie-task-1 config
      ansible.builtin.template:
        src: templates/charlie-task-1.j2
        dest: /etc/uniform/charlie-task-1.conf
        mode: '0644'

    # Description:
    # Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

    - name: Ensure golf-task-2 is present
      ansible.builtin.file:
        path: /opt/uniform/golf-task-2
        state: directory

    - name: Template golf-task-2 config
      ansible.builtin.template:
        src: templates/golf-task-2.j2
        dest: /etc/uniform/golf-task-2.conf
        mode: '0644'

    # Description:
    # Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. 

    - name: Ensure oscar-task-3 is present
      ansible.builtin.file:
        path: /opt/uniform/oscar-task-3
        state: directory

    - name: Template oscar-task-3 config
      ansible.builtin.template:
        src: templates/oscar-task-3.j2
        dest: /etc/uniform/oscar-task-3.conf
        mode: '0644'

    # Description:
    # Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

  handlers:
    - name: restart uniform service
      ansible.builtin.service:
        name: uniform
        state: restarted

## Notes

Excepteur sint occaecat cupidatat non proident, sunt in culpa. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. 

***
Generated: 2025-11-07T18:27:43Z
