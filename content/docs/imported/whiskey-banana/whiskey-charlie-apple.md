# Play: Whiskey - setup

- hosts: all
  become: true
  vars:
    app_name: "whiskey_app"
    retry_count: 3

  tasks:
    - name: Ensure mango-task-1 is present
      ansible.builtin.file:
        path: /opt/whiskey/mango-task-1
        state: directory

    - name: Template mango-task-1 config
      ansible.builtin.template:
        src: templates/mango-task-1.j2
        dest: /etc/whiskey/mango-task-1.conf
        mode: '0644'

    # Description:
    # Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. 

    - name: Ensure grape-task-2 is present
      ansible.builtin.file:
        path: /opt/whiskey/grape-task-2
        state: directory

    - name: Template grape-task-2 config
      ansible.builtin.template:
        src: templates/grape-task-2.j2
        dest: /etc/whiskey/grape-task-2.conf
        mode: '0644'

    # Description:
    # Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. 

    - name: Ensure mike-task-3 is present
      ansible.builtin.file:
        path: /opt/whiskey/mike-task-3
        state: directory

    - name: Template mike-task-3 config
      ansible.builtin.template:
        src: templates/mike-task-3.j2
        dest: /etc/whiskey/mike-task-3.conf
        mode: '0644'

    # Description:
    # Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. 

  handlers:
    - name: restart whiskey service
      ansible.builtin.service:
        name: whiskey
        state: restarted

## Notes

Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. 

***
Generated: 2025-11-07T18:27:43Z
