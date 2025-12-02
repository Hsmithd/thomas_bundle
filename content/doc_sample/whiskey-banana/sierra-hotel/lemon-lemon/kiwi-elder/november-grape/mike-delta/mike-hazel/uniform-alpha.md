# Play: Uniform - setup

- hosts: all
  become: true
  vars:
    app_name: "uniform_app"
    retry_count: 3

  tasks:
    - name: Ensure hotel-task-1 is present
      ansible.builtin.file:
        path: /opt/uniform/hotel-task-1
        state: directory

    - name: Template hotel-task-1 config
      ansible.builtin.template:
        src: templates/hotel-task-1.j2
        dest: /etc/uniform/hotel-task-1.conf
        mode: '0644'

    # Description:
    # Excepteur sint occaecat cupidatat non proident, sunt in culpa. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. 

    - name: Ensure mango-task-2 is present
      ansible.builtin.file:
        path: /opt/uniform/mango-task-2
        state: directory

    - name: Template mango-task-2 config
      ansible.builtin.template:
        src: templates/mango-task-2.j2
        dest: /etc/uniform/mango-task-2.conf
        mode: '0644'

    # Description:
    # Excepteur sint occaecat cupidatat non proident, sunt in culpa. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. 

  handlers:
    - name: restart uniform service
      ansible.builtin.service:
        name: uniform
        state: restarted

## Notes

Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

***
Generated: 2025-11-07T18:27:43Z
